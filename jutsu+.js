const titles_all = document.getElementsByClassName('anime_next_all')[0];
const substring = 'https://jut.su/oneepiece/episode-';

titles_all.forEach(title => {
    console.log(title.innerHTML);
});