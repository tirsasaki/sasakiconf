-- Bootstrap Lazy.nvim (resmi)
local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
if not vim.loop.fs_stat(lazypath) then
  vim.fn.system({
    "git", "clone", "--filter=blob:none",
    "https://github.com/folke/lazy.nvim.git",
    "--branch=stable", lazypath,
  })
end
vim.opt.rtp:prepend(lazypath)

-- (Opsional tapi disarankan) aktifkan true color
vim.opt.termguicolors = true

-- Plugins
require("lazy").setup({
  {
    "Mofiqul/dracula.nvim",
    lazy = false,        -- load saat startup
    priority = 1000,     -- load lebih awal dari plugin lain
    config = function()
      vim.cmd("colorscheme dracula")
    end,
  },
})

