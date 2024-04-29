// ==UserScript==
// @name         Steam Workshop calcuate collection size
// @namespace    http://tampermonkey.net/
// @version      2024-04-29
// @description  try to take over the world!
// @author       You
// @match        https://steamcommunity.com/sharedfiles/filedetails/?id=*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=steamcommunity.com
// @grant        none
// ==/UserScript==

let total = 0

async function sumSizes() {
    const divCollection = document.getElementsByClassName('collectionChildren')[0]
    const divItems = divCollection.getElementsByClassName('collectionItem')
    const count = divItems.length
    let data = {'itemcount': count}

    for (let i = 0; i < count; i++) {
        data[`publishedfileids[${i}]`] = divItems[i].id.split('sharedfile_')[1]
    }

    await fetch('https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: data
    })
        .then((response) => response.json())
        .then(function(json) {
            for (const item of Array.from(json.response.items)) {
                total += item.file_size
            }
        }).catch((err) => console.warn('Something went wrong.', err));
}

(function() {
    'use strict';
    sumSizes().then(function() {
        if (total) {
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
