vidID = 0;
var app;
var vidID = 0;

$(document).ready(function () {
    app = new Vue({
        el: '#app',
        data: function() {
            return {
                board: board,
                thread: thread,
                duration: 0,
                currentTime: 0,
                tim: posts[0].tim,
                filename: posts[0].filename
            }
        },
        computed: {
            VideoURL: function () {
                return "https://i.4cdn.org/"+this.board+"/"+this.tim+".webm";
            },

            PercentageComplete: function () {
                return (this.currentTime / this.duration) * 100
            }
        }
    });

    var vid = document.getElementById("mainvid");
    vid.addEventListener('timeupdate',function(){
        app.currentTime = vid.currentTime;
        app.duration = vid.duration;
    });

    vid.addEventListener('ended', function () {
        nextVideo();
    })


});

function nextVideo() {
    vidID++;
    updateVid()
}

function prevVideo() {
    vidID--;
    updateVid()
}


function updateVid(){
    app.tim = posts[vidID].tim;
    app.filename = posts[vidID].filename;
    document.getElementById("mainvid").load()
}