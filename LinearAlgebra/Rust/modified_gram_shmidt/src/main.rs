// In Rust, we explicitly import types and functions we want to use from other libraries (crates).
// This is similar to `import numpy as np`. Here, we're importing the `DMatrix` type
// from the `nalgebra` crate, which is a dynamically sized matrix.
use nalgebra::DMatrix
// --- Function Definition ---
// This is the Rust equivalent of `def modified_gramschmidt(A : np.array) -> list[np.array, np.array]:`
//
// fn: Keyword to define a function.
// modified_gram_schmidt: The function name.
// a: The input parameter name.
// &DMatrix<f64>: The type of the input.
//   - DMatrix<f64>: A matrix of 64-bit floating-point numbers (like numpy's float64).
//   - &: This is a "borrow". It means we are taking the matrix by reference instead of
//        taking ownership (making a full copy). This is more efficient.
// -> Result<(DMatrix<f64>, DMatrix<f64>), &'static str>: The return type.
//   - In Rust, functions can only have one return value. To return multiple items, we group them
//     in a "tuple", like `(Q, R)`.
//   - `Result<T, E>` is a special enum used for error handling. It can either be:
//     - `Ok(T)`: The operation succeeded, containing the value `T`.
//     - `Err(E)`: The operation failed, containing an error `E`.
//     This is how Rust handles exceptions, forcing the programmer to deal with potential failures.
//     Here, a success returns a tuple of two matrices, and an error returns a string slice.
fn modified_gramschmidt(a: &DMatrix<f64>) -> Result<(DMatrix<f64>, DMatrix<f64>), &'static str> {
    // Get the dimensions of the input matrix `a`.
    let (nrows, ncols) = a.shape();

    // --- Precompute memory ---
    // `let mut` declares a mutable variable. In Rust, variables are immutable by default.
    // This is equivalent to `Q = np.zeros(A.shape)`.
    let mut q = DMatrix::<f64>::zeros(nrows, ncols);
    // This is equivalent to `R = np.zeros((n,n))`.
    let mut r = DMatrix::<f64>::zeros(ncols, ncols);

    // Define a small tolerance for zero-check, just like in the Python code.
    let tolerance = 1e-10;

    // --- Main Loop ---
    // `for j in 0..ncols` is Rust's equivalent of `for j in np.arange(0,n):`.
    // It creates a loop that iterates from 0 up to (but not including) `ncols`.
    for j in 0..ncols {
        // Get a copy of the j-th column of matrix A.
        // `.column(j)` gets a reference to the column.
        // `.into_owned()` creates a mutable copy, similar to Python's `.copy()`.
        let mut v = a.column(j).into_owned();

        // --- Inner Loop ---
        for i in 0..j {
            // Calculate the dot product. This is equivalent to `R[i,j] = np.dot(Q[:,i],v)`.
            // Note that matrix indexing in nalgebra uses a tuple `(row, col)`.
            r[(i, j)] = q.column(i).dot(&v);

            // Update the vector v. This is equivalent to `v = v - R[i,j]*Q[:,i]`.
            v -= r[(i, j)] * q.column(i);
        }

        // Calculate the norm of the vector v. Equivalent to `np.linalg.norm(v)`.
        let norm_v = v.norm();
        r[(j, j)] = norm_v;

        // --- FIX: Check for zero norm before dividing ---
        if norm_v < tolerance {
            // Instead of raising an exception, we return the `Err` variant of our `Result`.
            // This signals to the calling function that something went wrong.
            return Err("Matrix has linearly dependent columns.");
        }

        // Normalize the j-th column of Q. Equivalent to `Q[:,j] = v / R[j,j]`.
        q.set_column(j, &(v / norm_v));
    }

    // If the function completes successfully, we wrap our tuple `(q, r)` in the `Ok`
    // variant of the `Result` and return it.
    Ok((q, r))
}

// --- Main Function ---
// This is the entry point of our program, just like `if __name__ == "__main__":` in Python.
fn main() {
    // Create a matrix. `DMatrix::from_row_slice` creates a matrix from a flat array of data.
    // We specify the number of rows (3) and columns (3).
    let a = DMatrix::from_row_slice(3, 3, &[
        1.0, 2.0, 3.0,
        4.0, 5.0, 6.0,
        7.0, 8.0, 11.0,
    ]);

    println!("Original Matrix A:\n{}", a);

    // Call our function. Since it returns a `Result`, we need to handle both cases.
    // `match` is a powerful control flow construct in Rust that is perfect for this.
    match modified_gramschmidt(&a) {
        // If the result is Ok, we "destructure" it to get the q and r matrices.
        Ok((q, r)) => {
            println!("\nCalculated Q:\n{}", q);
            println!("\nCalculated R:\n{}", r);
            println!("\nQ * R:\n{}", q * r);
        }
        // If the result is Err, we get the error message and print it.
        Err(e) => {
            eprintln!("\nError: {}", e);
        }
    }
}

fn main(){
    let input_Matrix = DMatrix::from_row_slice(3,3,)
}