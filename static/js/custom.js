function send_comment(article_id) {
    let hidden_input = $('#set_parent_comment').val()
    let text = $('#comment').val()
    $.get('/article/send-comment/', {
        'text': text,
        'article_id': article_id,
        'parent': hidden_input
    }).then(
        res => {
            if (res.status === 'anwser-success') {
                Swal.fire({
                    title: "پاسخ شما ثبت شد و پس از تایید نشان داده می شود",
                    // text: "You clicked the button!",
                    icon: "success"
                });
            } else if (res.status === 'success') {
                Swal.fire({
                    title: "کامنت شما ثبت شد و پس از تایید نشان داده می شود",
                    // text: "You clicked the button!",
                    icon: "success"
                });
            } else if (res === 'id-error') {
                Swal.fire("آره داداش منم هندلش نکردم");
            }
        }
    )
}

function set_parent(comment_id) {
    document.getElementById('scroll-to').scrollIntoView({behavior: 'smooth'})
    let hidden_input = $('#set_parent_comment')
    hidden_input.val(comment_id)
}

function comment_likes(comment_id, like) {
    $.get('/article/add-comment-like/', {
        'comment_id': comment_id,
        'like': like
    }).then(
        res => {
            location.reload()
        }
    )
}

function subcomment_likes(comment_id, like) {
    $.get('/article/add-comment-like/', {
        'comment_id': comment_id,
        'like': like
    }).then(
        res => {
            location.reload()
        }
    )
}

function product_wishlist(product_id) {
    $.get('/products/add-to-wishlist/', {
        'product_id': product_id,
    }).then(
        res => {
            if (res.status === 'success') {
                Swal.fire("محصول به علاقه مندی ها اضافه شد");
            } else if (res.status === 'deleted') {
                Swal.fire("محصول از علاقه مندی ها حذف شد");
            } else if (res === 'id-error') {
                Swal.fire("آره داداش منم هندلش نکردم");
            }
        }
    )
}

function delete_wishlist(product_id) {
    $.get('/dashbord/delete-wishlist-product/', {
        'product_id': product_id
    }).then(
        res => {
            if (res.status === 'success') {
                Swal.fire("محصول از علاقه مندی ها حذف شد");
            } else if (res === 'id-error') {
                Swal.fire("آره داداش منم هندلش نکردم");
            }
        }
    )
}

function add_notif(product_id) {
    $.get('/products/add-notif/', {
        'product_id': product_id
    }).then(
        res => {
            if (res.status === 'success') {
                Swal.fire("زمانی که محصول موجود شد در حساب کاربری به شما اطلاع می دهیم");
            } else if (res.status === 'deleted') {
                Swal.fire("دیگر به شما اطلاع نمی دهیم");
            } else if (res.status === 'id-error') {
                Swal.fire("آره داداش منم هندلش نکردم");
            }
        }
    )
}

// function product_categories(){
//     let response = $('#response-area')
//     let most_visited = $('#Most-visited-tab').val()
//     let most_sells = $('#Bestselling-tab').val()
//     let most_new = $('#newest-tab').val()
//     let most_cheap = $('#cheapest-tab').val()
//     let most_expensive = $('#most-expensive-tab').val()
//     $.get('/products/change-category/' , {
//         'most_visited':most_visited,
//         'most_sells':most_sells,
//         'most_new':most_new,
//         'most_cheap':most_cheap,
//         'most_expensive':most_expensive
//     }).then(
//         res=>{
//             response.html(res.body)
//         }
//     )
// }

function product_comments(product_id) {
    let hidden_input = $('#product_set_parent').val()
    let text = $('#comment').val()
    $.get('/products/send-comment/', {
        'parent': hidden_input,
        'text': text,
        'product_id': product_id
    }).then(
        res => {
            if (res.status === 'anwser-success') {
                Swal.fire({
                    title: "پاسخ شما ثبت شد و پس از تایید نشان داده می شود",
                    // text: "You clicked the button!",
                    icon: "success"
                });
            } else if (res.status === 'success') {
                Swal.fire({
                    title: "کامنت شما ثبت شد و پس از تایید نشان داده می شود",
                    // text: "You clicked the button!",
                    icon: "success"
                });
            } else if (res === 'id-error') {
                Swal.fire("آره داداش منم هندلش نکردم");
            }
        }
    )
}

function product_set_parent(comment_id){
    document.getElementById('scroll-to').scrollIntoView({behavior: 'smooth'})
    let hidden_input = $('#product_set_parent')
    hidden_input.val(comment_id)
}
