$('#like').click(function(){
    var postid;
    postid = $(this).attr("data-postid");
    $.get('/blog/like_post/', {postid: postid}, function(data){
        $("#unlike").show();
	$("#unlike").html(data);
        $("#like").hide();
    });
});
