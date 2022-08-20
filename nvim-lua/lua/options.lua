local wo = vim.wo
local o = vim.o
local cmd = vim.cmd



-- Use the default system Clipboard
o.clipboard = "unnamedplus"

-- set linenumber
wo.number = true
wo.rnu = true

-- set tabsize
o.tabstop = 4
o.shiftwidth = 4
o.expandtab = true
o.autoindent = true
o.undofile = true
o.cursorline = true

wo.colorcolumn = '80'

-- indent
o.autoindent = true
o.cursorline = true
o.autowrite = true
o.autoread = true

o.scrolloff = 10

-- Start gitcommit in Insert Mode
vim.api.nvim_create_augroup("bufcheck", { clear = true })
vim.api.nvim_create_autocmd("FileType", {
    group = "bufcheck",
    pattern = { "gitcommit", "gitrebase" },
    command = "startinsert | 1",
})

-- wider Lines for Markdown and auto Linebreak.. Oh and Spellcheck 
vim.api.nvim_create_autocmd(
    { "BufRead", "BufNewFile" },
    { pattern = { "*.md"}, command = "set cc=120 tw=120" }
)
vim.api.nvim_create_autocmd(
    { "BufRead", "BufNewFile" },
    { pattern = { "*.md"}, command = ":setlocal spell complete+=kspell spelllang=en_gb,en_us,de_de" }
)

-- go Highlighting
--
