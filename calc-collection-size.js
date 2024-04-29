// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      2024-04-29
// @description  try to take over the world!
// @author       You
// @match        https://steamcommunity.com/sharedfiles/filedetails/?id=*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=steamcommunity.com
// @grant        none
// ==/UserScript==

let itemsFinished = 0
let total = 0

async function getSize(url) {
    await fetch(url)
        .then((response) => response.text())
        .then(function(html) {
            // Convert the HTML string into a document object
            const parser = new DOMParser();
            const doc = parser.parseFromString(html, 'text/html');
            const fileSizeDetails = doc.getElementsByClassName('detailsStatRight')[0].innerHTML.split(' ') // 0 - number, 1 - type

            let size = parseFloat(fileSizeDetails[0]); // Bytes
            switch (fileSizeDetails[1]) {
                case 'b':
                    size /= 8
                    break
                case 'B':
                    break
                case 'KB':
                    size *= 1000
                    break
                case 'MB':
                    size *= 1e6
                    break
                case 'GB':
                    size *= 1e9
                    break
                default:
                    console.log(`default case (${fileSizeDetails[0]}, ${fileSizeDetails[1]}, ${url})`)
                    break;
            }
            total += size
        }).catch((err) => console.warn('Something went wrong.', err));
}

async function sumSizes() {
    const divCollection = document.getElementsByClassName('collectionChildren')[0]
    const divItems = divCollection.getElementsByClassName('collectionItem')
    const count = divItems.length

    for (const item of Array.from(divItems)) {
        const url = item.getElementsByClassName('workshopItem')[0].children[0].href
        await getSize(url)
        if (++itemsFinished % 100 == 0) console.log(`calculation size progress: ${itemsFinished}/${count}`)
    };
}

(function() {
    'use strict';
    sumSizes().then(function() {
        if (itemsFinished) {
            const gb = total / 1e9
            const mb = gb * 1000
            const kb = mb * 1000
            const bytes = kb * 1000

            if (Math.floor(gb) > 1) console.log(`collection size: ${gb} GB`)
            else if (Math.floor(mb) > 1) console.log(`collection size: ${mb} MB`)
            else if (Math.floor(kb) > 1) console.log(`collection size: ${kb} KB`)
            else console.log(`collection size: ${bytes} Bytes`)
        }
    })
})();
