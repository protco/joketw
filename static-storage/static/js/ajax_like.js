//add
// <a class="likebutton" id="like{{joke.id}}" href="#" data-catid="{{ joke.id }}"><span class="glyphicon glyphicon-heart"></a>
// to a joke
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>

<script type="text/javascript">
    $('.likebutton').click(function(){
        var catid;
        catid = $(this).attr("data-catid");
        $.ajax({
            type:"GET", url: "/likejoke", data:{ joke_id: catid},
            success: function( data )
            { $( '#like'+ catid ).remove(); $( '#message' ).text(data);}
        })
    });
</script>
