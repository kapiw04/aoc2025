local stdin = "input.txt"
local prg = string.format("python3 %% < $(dirname %%)/%s", stdin)

vim.o.makeprg = prg

local function set_stdin(name)
	local prg = string.format("python3 %% < $(dirname %%)/%s", name)
	vim.o.makeprg = prg
	vim.g.aoc_stdin = name
	print("stdin -> " .. name)
end

set_stdin(stdin)

vim.keymap.set("n", "<leader>i", function()
	if stdin == "input.txt" then
		stdin = "example.txt"
	else
		stdin = "input.txt"
	end
	print(stdin)
	set_stdin(stdin)
end, { desc = "Set stdin for :make" })
