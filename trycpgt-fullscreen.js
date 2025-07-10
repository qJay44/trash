// ==UserScript==
// @name         trycgpt fullscreen
// @namespace    http://tampermonkey.net/
// @version      2025-06-19
// @description  try to take over the world!
// @author       You
// @match        https://trychatgpt.ru/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=trychatgpt.ru
// @grant        none
// ==/UserScript==

(function() {
  'use strict';
  const parent = document.getElementById('root')
  const copyWhat = document.querySelector("#root > div > main")
  const copyWhatCss = document.querySelector("#root > div > link")
  const deleteWhat = document.querySelector("#root > div")

  // The main div
  copyWhat.classList.remove('py-6')

  // The div of the sidebar and the chat (inside the main div)
  copyWhat.firstChild.classList.remove('!min-h-[550px]')
  copyWhat.firstChild.classList.remove('max-w-[1400px]')

  // The chat
  copyWhat.firstChild.lastChild.classList.remove('max-w-[1400px]')
  copyWhat.firstChild.lastChild.classList.remove('!min-h-[calc(550px-theme(spacing.4))]')

  parent.appendChild(copyWhat)
  parent.appendChild(copyWhatCss)
  parent.removeChild(deleteWhat)
})();

