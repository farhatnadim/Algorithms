import Lake
open Lake DSL

package «algorithms» where
  -- Settings applied to both the library and executable
  leanOptions := #[
    ⟨`pp.unicode.fun, true⟩
  ]

lean_lib «Algorithms» where
  -- Library configuration

@[default_target]
lean_exe «algorithms» where
  root := `Main
