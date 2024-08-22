document.querySelector('.search-bar input').addEventListener('focus', () => {
    document.querySelector('.navbar').style.boxShadow = "0 4px 10px rgba(0, 0, 0, 0.4)";
});

document.querySelector('.search-bar input').addEventListener('blur', () => {
    document.querySelector('.navbar').style.boxShadow = "0 2px 5px rgba(0, 0, 0, 0.2)";
});
