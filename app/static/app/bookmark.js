'use strict';

console.log("bookmark.js")

// create click event target
document.addEventListener('click', (evt) => {
    const bookmarkBtn = evt.target.closest('#bookmark');
    console.log("button is clicked");
    
    var userIsAuthenticated = document.querySelector('#hidden-is-authenticated').value
    const postId = bookmarkBtn.getAttribute("post-id")
    // console.log(postId)

    const csrfToken = bookmarkBtn.getAttribute("csrfmiddlewaretoken")
    // console.log(csrfToken)

    if (userIsAuthenticated){
        fetch(`/bookmark_post/${postId}`,{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            mode: 'same-origin'
        })
        .then((response)=> response.json())
        .then((responseJson)=> {
            console.log(`bookmarked = ${responseJson.bookmarked}`)
            var i_el = document.getElementById("marked")
            console.log(i_el)

            if(responseJson.bookmarked) {                
                i_el.classList.remove('uil')
                i_el.classList.remove('uil-bookmark-full');
                
                i_el.classList.add('fa-solid')
                i_el.classList.add('fa-bookmark');
            } else {
                i_el.classList.remove('fa-solid')
                i_el.classList.remove('fa-bookmark');
                
                i_el.classList.add('uil')
                i_el.classList.add('uil-bookmark-full');
            }
        })
    }
})
