call plug#begin()
Plug 'fatih/vim-go'
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'sainnhe/everforest'
Plug 'NLKNguyen/Papercolor-theme'
Plug 'sainnhe/sonokai'
Plug 'mboughaba/i3config.vim'
Plug 'preservim/nerdtree'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'isobit/vim-caddyfile'
Plug 'yaegassy/coc-ansible', {'do': 'yarn install --frozen-lockfile'}
Plug 'dense-analysis/ale'
Plug 'ap/vim-css-color'
call plug#end()
" Beginn Colorscheme
if has('termguicolors')
  set termguicolors
endif
set background=dark
let g:everforest_background = 'hard'
let g:everforest_better_performance = 1
let g:sonokai_style = 'atlantis'
let g:sonokai_better_performance = 1
colorscheme sonokai
" End Colorscheme
" Beginn Airline
let g:airline_powerline_fonts = 1
if !exists('g:airline_symbols')
	let g:airline_symbols = {}
endif
let g:airline_symbols.space = "\ua0"
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#show_buffers = 0
let g:airline_theme = 'molokai'

" End Airline	

" Spell-check Markdown files and Git Commit Messages
set nospell
autocmd FileType markdown setlocal spell spelllang=en_us,de_de
autocmd FileType gitcommit setlocal spell spelllang=en_us,de_de

"setlocal spell spelllang=en_us,de_de
autocmd FileType markdown setlocal complete+=kspell spelllang=en_us,de_de
autocmd FileType gitcommit setlocal complete+=kspell spelllang=en_us,de_de
set number relativenumber
set textwidth=80
set colorcolumn=80
set cursorline
highlight clear CursorLine

set tabstop=4
set shiftwidth=4
set softtabstop=0 expandtab	

" Coc Keymappings (Tab = Shift Tab for Scrolling through corretions, Enter to
" complete)
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"
inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"

let g:coc_filetype_map = {
  \ 'yaml.ansible': 'ansible',
  \ }
"Set default Clipboard to systemwide - Aka fix Copy Paste
set clipboard+=unnamedplus

filetype on
filetype indent on
filetype plugin on


syntax on
set autoindent

let g:go_auto_sameids = 0
let g:go_highlight_types = 1
let g:go_highlight_fields = 1
let g:go_highlight_functions = 1
let g:go_highlight_function_calls = 1
let g:go_highlight_operators = 1
let g:go_highlight_extra_types = 1
let g:go_highlight_build_constraints = 1
let g:go_highlight_generate_tags = 1

"NERDTree
nmap <C-f> :NERDTreeToggle<CR>
"autocmd VimEnter * NERDTree | wincmd p
" Exit Vim if NERDTree is the only window remaining in the only tab.
autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif


" Source Custom Configs
source $HOME/.config/nvim/extra.vim
