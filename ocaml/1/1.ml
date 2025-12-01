let read_text_from_stdin =
    In_channel.with_open_text
      "/dev/stdin"
       In_channel.input_all

let get_lines text = 
    String.split_on_char
        '\n'
        text

let parse_direction line = 
    String.get
        line
        0

let parse_n line = 
    Stdlib.int_of_string (
    String.sub
        line
        1
        (String.length line - 1)
    )

let rec parse_lines lines =
    match lines with
     | [] -> []
     | line::rest -> (parse_direction line, parse_n line) :: parse_lines rest

let (%%) a b = 
    let r = a mod b in
    if r < 0 then r + b else r

let rec step cur_rot count pairs = 
    (* Printf.printf "cur_rot: %d\n" cur_rot; *)
    let new_count = if cur_rot == 0 then count + 1 else count in 
    
    match pairs with 
     | [] -> new_count
     | pair::rest -> 
        match Stdlib.Pair.fst pair with
        | 'L' -> step ((cur_rot + -1 * Stdlib.Pair.snd pair) %% 100) new_count rest
        | 'R' -> step ((cur_rot +  1 * Stdlib.Pair.snd pair) %% 100) new_count rest
        | _ -> 0

let lines_from_stdin = 
    read_text_from_stdin
    |> get_lines

let() =
    lines_from_stdin
    |> parse_lines 
    |> step 50 0
    |> print_int

let() = print_endline ""
