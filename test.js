const user = '&user=q44l';
const api_key = '&api_key=f756432e1e81a98cbe4d6d7adfcc2b86';

const mbid = '&mbid=';
const format = '&format=';
const requestURL = 'https://ws.audioscrobbler.com/2.0/?method=';

function track_getInfo() {
    let curr_method = 'track.getInfo';
    let curr_mbid = mbid + 'ebf79ba5-085e-48d2-9eb8-2d992fbf0f6d';
    let curr_format = format + 'json';

    let result = requestURL
        + curr_method
        + api_key
        + curr_mbid
    console.log(result); 
    sendRequest(result);
}

function sendRequest(url) {
    const request = new XMLHttpRequest();
    request.open('POST', url)
    request.responseType = 'json';
    request.send();
    request.onload = function() {
        const userInfo = request.response;
        console.log(userInfo);
    }
}

track_getInfo();