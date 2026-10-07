const urlParams = new URLSearchParams(window.location.search);

if (urlParams.has('failed')) {
    alert('The password you provided was incorrect!');
}