//! portpal parity runner (Rust): reads a fixture JSON, runs every case
//! through the user-written algorithm crates, prints one JSON array of
//! `{"name", "output"|"error"}` entries to stdout.
//!
//! Dispatch/JSON glue only — no algorithm logic (see CLAUDE.md carve-out).

use serde_json::{json, Map, Value};
use std::env;
use std::fs;
use std::process::ExitCode;

type DispatchResult = Result<Value, String>;

fn int_vec(v: &Value) -> Result<Vec<i64>, String> {
    v.as_array()
        .ok_or_else(|| "expected an integer array".to_string())?
        .iter()
        .map(|x| {
            x.as_i64()
                .ok_or_else(|| format!("expected integer, got {x}"))
        })
        .collect()
}

fn int_matrix(v: &Value) -> Result<Vec<Vec<i64>>, String> {
    v.as_array()
        .ok_or_else(|| "expected a matrix (array of arrays)".to_string())?
        .iter()
        .map(int_vec)
        .collect()
}

fn float_matrix(v: &Value) -> Result<Vec<Vec<f64>>, String> {
    v.as_array()
        .ok_or_else(|| "expected a matrix (array of arrays)".to_string())?
        .iter()
        .map(|row| {
            row.as_array()
                .ok_or_else(|| "expected a matrix row".to_string())?
                .iter()
                .map(|x| {
                    x.as_f64()
                        .ok_or_else(|| format!("expected number, got {x}"))
                })
                .collect()
        })
        .collect()
}

fn field<'a>(input: &'a Value, key: &str) -> Result<&'a Value, String> {
    input
        .get(key)
        .ok_or_else(|| format!("missing input field {key:?}"))
}

fn usize_field(input: &Value, key: &str) -> Result<usize, String> {
    field(input, key)?
        .as_u64()
        .map(|n| n as usize)
        .ok_or_else(|| format!("input field {key:?} must be a non-negative integer"))
}

fn str_field<'a>(input: &'a Value, key: &str) -> Result<&'a str, String> {
    field(input, key)?
        .as_str()
        .ok_or_else(|| format!("input field {key:?} must be a string"))
}

fn dispatch(algorithm: &str, input: &Value) -> DispatchResult {
    match algorithm {
        "insertion_sort" => {
            let mut arr = int_vec(field(input, "array")?)?;
            algorithms_sort::insertion_sort(&mut arr);
            Ok(json!(arr))
        }
        "bubble_sort" => {
            let mut arr = int_vec(field(input, "array")?)?;
            algorithms_sort::bubble_sort(&mut arr);
            Ok(json!(arr))
        }
        "merge_sort" => {
            let mut arr = int_vec(field(input, "array")?)?;
            algorithms_sort::merge_sort(&mut arr);
            Ok(json!(arr))
        }
        "quick_sort" => {
            let mut arr = int_vec(field(input, "array")?)?;
            algorithms_sort::quick_sort(&mut arr);
            Ok(json!(arr))
        }
        "r_select" => {
            let mut arr = int_vec(field(input, "array")?)?;
            let ith = usize_field(input, "ith")?;
            Ok(json!(algorithms_select::r_select(&mut arr, ith)))
        }
        "d_select" => {
            let mut arr = int_vec(field(input, "array")?)?;
            let ith = usize_field(input, "ith")?;
            Ok(json!(algorithms_select::d_select(&mut arr, ith)))
        }
        "binary_search" => {
            let arr = int_vec(field(input, "array")?)?;
            let target = field(input, "target")?
                .as_i64()
                .ok_or_else(|| "input field \"target\" must be an integer".to_string())?;
            Ok(json!(algorithms_search::binary_search(&arr, &target)))
        }
        "second_largest" => {
            let arr = int_vec(field(input, "array")?)?;
            Ok(json!(algorithms_search::second_largest(&arr)))
        }
        "count_inversions" => {
            let mut arr = int_vec(field(input, "array")?)?;
            Ok(json!(algorithms_misc::count_inversions(&mut arr)))
        }
        "standard_multiply" => {
            let x = str_field(input, "x")?;
            let y = str_field(input, "y")?;
            Ok(json!(algorithms_integer_mult::standard_multiply(x, y)))
        }
        "karatsuba_multiply" => {
            let x = str_field(input, "x")?;
            let y = str_field(input, "y")?;
            Ok(json!(algorithms_integer_mult::karatsuba_multiply(x, y)))
        }
        "vec_dot" => {
            let a = int_vec(field(input, "a")?)?;
            let b = int_vec(field(input, "b")?)?;
            Ok(json!(algorithms_linear_algebra::vec_dot(&a, &b)))
        }
        "mat_mul" => {
            let a = int_matrix(field(input, "a")?)?;
            let b = int_matrix(field(input, "b")?)?;
            Ok(json!(algorithms_linear_algebra::mat_mul(&a, &b)))
        }
        "rec_mat_mul" => {
            let a = int_matrix(field(input, "a")?)?;
            let b = int_matrix(field(input, "b")?)?;
            Ok(json!(algorithms_linear_algebra::rec_mat_mul(&a, &b)))
        }
        "strassen" => {
            let a = int_matrix(field(input, "a")?)?;
            let b = int_matrix(field(input, "b")?)?;
            Ok(json!(algorithms_linear_algebra::strassen(&a, &b)))
        }
        "modified_gram_schmidt" => {
            let a = float_matrix(field(input, "a")?)?;
            match algorithms_linear_algebra::modified_gram_schmidt(&a) {
                Some((q, r)) => Ok(json!({"q": q, "r": r})),
                None => Ok(Value::Null),
            }
        }
        other => Err(format!("unknown algorithm {other:?}")),
    }
}

fn main() -> ExitCode {
    let args: Vec<String> = env::args().collect();
    let Some(path) = args.get(1) else {
        eprintln!("usage: parity_runner <fixture.json>");
        return ExitCode::from(2);
    };
    let text = match fs::read_to_string(path) {
        Ok(t) => t,
        Err(e) => {
            eprintln!("cannot read {path}: {e}");
            return ExitCode::from(2);
        }
    };
    let fixture: Value = match serde_json::from_str(&text) {
        Ok(v) => v,
        Err(e) => {
            eprintln!("invalid fixture JSON: {e}");
            return ExitCode::from(2);
        }
    };

    let algorithm = fixture["algorithm"]
        .as_str()
        .unwrap_or_default()
        .to_string();
    let empty = Vec::new();
    let cases = fixture["cases"].as_array().unwrap_or(&empty);

    let mut results = Vec::new();
    for case in cases {
        let mut entry = Map::new();
        entry.insert("name".to_string(), case["name"].clone());
        match dispatch(&algorithm, &case["input"]) {
            Ok(output) => entry.insert("output".to_string(), output),
            Err(e) => entry.insert("error".to_string(), json!(e)),
        };
        results.push(Value::Object(entry));
    }
    println!("{}", Value::Array(results));
    ExitCode::SUCCESS
}
