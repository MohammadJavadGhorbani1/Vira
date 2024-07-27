
function send_comment(article_id){
    let hidden_input = $('#set_parent_comment').val()
    let text = $('#comment').val()
    $.get('/article/send-comment/' , {
        'text':text,
        'article_id':article_id,
        'parent':hidden_input
    }).then(
        res => {
            location.reload()
        }
    )
}

function set_parent(comment_id){
    document.getElementById('scroll-to').scrollIntoView({behavior:'smooth'})
    let hidden_input = $('#set_parent_comment')
    hidden_input.val(comment_id)
}

function comment_likes(comment_id , like){
    $.get('/article/add-comment-like/' , {
        'comment_id':comment_id,
        'like':like
    }).then(
        res=>{
            location.reload()
        }
    )
}

function subcomment_likes(comment_id , like){
    $.get('/article/add-comment-like/' , {
        'comment_id':comment_id,
        'like':like
    }).then(
        res=>{
            location.reload()
        }
    )
}