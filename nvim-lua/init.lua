require('keys')
require('plugins')
require('options')
--require('lsp')

require("nvim-lsp-installer").setup {}


-- docker
require'lspconfig'.dockerls.setup{}

-- markdown
require'lspconfig'.marksman.setup{}
-- Java
require'lspconfig'.jdtls.setup{}
-- nvim-go
require('go').setup({})
require'lspconfig'.gopls.setup{}

require'nvim-treesitter.configs'.setup {
  ensure_installed = "all",
  highlight = {
    enable = true
  },
}



-- python
require'lspconfig'.jedi_language_server.setup{}
require'lspconfig'.pyright.setup{}

-- cue
require'lspconfig'.dagger.setup{}

-- yaml
require('lspconfig').yamlls.setup {
  settings = {
    yaml = {
      schemas = {
        ["https://json.schemastore.org/github-workflow.json"] = "/.github/workflows/*",
        ["../path/relative/to/file.yml"] = "/.github/workflows/*",
        ["/path/from/root/of/project"] = "/.github/workflows/*",
      },
    },
  }
}

-- lua
require'lspconfig'.sumneko_lua.setup {
  settings = {
    Lua = {
      runtime = {
        version = 'LuaJIT',
      },
      diagnostics = {
        globals = {'vim'},
      },
      workspace = {
        library = vim.api.nvim_get_runtime_file("", true),
      },
      telemetry = {
        enable = false,
      },
    },
  },
}

require("luasnip.loaders.from_vscode").lazy_load()
