'use strict';

console.log("likes.js")
// create click event target
document.addEventListener('click', (evt) => {
    const favBtn = evt.target.closest('#fav');
    console.log("button is clicked");
    
    var userIsAuthenticated = document.querySelector('#hidden-is-authenticated').value
    const postId = favBtn.getAttribute("post-id")
    // console.log(postId)

    const csrfToken = favBtn.getAttribute("csrfmiddlewaretoken")
    // console.log(csrfToken)

    if (userIsAuthenticated){
        fetch(`/like_post/${postId}`,{
            method: 'POST',
            // body: JSON.stringify({post_id: postId}),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            mode: 'same-origin'
        })
        .then((response)=> response.json())
        .then((responseJson)=> {
            console.log(`liked = ${responseJson.liked}`)
            var i_el = document.getElementById("heart")
            console.log(i_el)

            if(responseJson.liked) {                
                i_el.classList.remove('uil')
                i_el.classList.remove('uil-heart');
                
                i_el.classList.add('fa-solid')
                i_el.classList.add('fa-heart');
            } else {
                i_el.classList.remove('fa-solid')
                i_el.classList.remove('fa-heart');
                
                i_el.classList.add('uil')
                i_el.classList.add('uil-heart');
            }
            var spanEl = document.getElementById("likes-count")
            spanEl.innerHTML = responseJson.likes_count
            }
        )
    }
})
