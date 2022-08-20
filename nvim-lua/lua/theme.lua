-- Set Nord Theme to look better
local o = vim.opt

o.termguicolors = true

-- Default options
require('nightfox').setup({
  options = {
    transparent = true,
    styles = {
      comments = "italic",
      keywords = "bold",
      types = "italic,bold",
    }
  }
})

vim.cmd[[colorscheme nordfox]]
