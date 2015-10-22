import webbrowser
import os
import re

# The filpping animation is refering to Udacity Nanodegree Page (https://www.udacity.com/nanodegree)

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link href='https://fonts.googleapis.com/css?family=Lato:300,100italic' rel='stylesheet' type='text/css'>
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        * {
            font-family: 'Lato', sans-serif;
        }
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        /*.movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }*/
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        //The below code is what I refer to Udacity Nanodegree Page
        .flip-container {
          -webkit-perspective: 1000;
          -moz-perspective: 1000;
          -o-perspective: 1000;
          perspective: 1000;
        }
        .flip-container {
          text-decoration: none;
          color: #303030;
        }
        .flip-container,
        .front,
        .back {
          position: relative;
          padding: 15px;
          margin: 0 auto;
          width: 320px;
          /*height: 150px;*/
          height: 440px;
        }
        @media (min-width: 768px) {
          @media -sass-debug-info{filename{font-family:file\:\/\/\/var\/lib\/jenkins\/jobs\/udacityu-PROD-STAGING\/workspace\/udacityu\/static\/css\/udacity\/base\.less}line{font-family:\000031000}}
          .flip-container,
          .front,
          .back {
            width: 300px;
            /*height: 230px;*/
            height: 440px;
          }
        }
        @media (min-width: 992px) {
          @media -sass-debug-info{filename{font-family:file\:\/\/\/var\/lib\/jenkins\/jobs\/udacityu-PROD-STAGING\/workspace\/udacityu\/static\/css\/udacity\/base\.less}line{font-family:\000031004}}
          .flip-container,
          .front,
          .back {
            margin: 15px;
            width: 320px;
            /*height: 275px;*/
            height: 440px;
          }
        }

        .flipper {
          -moz-transform: perspective(1000px);
          -moz-transform-style: preserve-3d;
          position: relative;
        }

        .front,
        .back {
          -webkit-backface-visibility: hidden;
          -moz-backface-visibility: hidden;
          -o-backface-visibility: hidden;
          backface-visibility: hidden;
          -webkit-transition: 0.6s;
          -webkit-transform-style: preserve-3d;
          -moz-transition: 0.6s;
          -moz-transform-style: preserve-3d;
          -o-transition: 0.6s;
          -o-transform-style: preserve-3d;
          -ms-transition: 0.6s;
          -ms-transform-style: preserve-3d;
          transition: 0.6s;
          transform-style: preserve-3d;
          position: absolute;
          top: 0;
        }

        .back {
          -webkit-transform: rotateY(-180deg);
          -moz-transform: rotateY(-180deg);
          -o-transform: rotateY(-180deg);
          -ms-transform: rotateY(-180deg);
          transform: rotateY(-180deg);
          background: #ffffff;
          color: #000000;
          /*color: gray;*/
          border-bottom: 15px solid;
        }

        .flip-container:hover .back,
        .flip-container.hover .back {
          -webkit-transform: rotateY(0deg);
          -moz-transform: rotateY(0deg);
          -o-transform: rotateY(0deg);
          -ms-transform: rotateY(0deg);
          transform: rotateY(0deg);
        }

        .flip-container:hover .front,
        .flip-container.hover .front {
          -webkit-transform: rotateY(180deg);
          -moz-transform: rotateY(180deg);
          -o-transform: rotateY(180deg);
          transform: rotateY(180deg);
        }
        .btn-primary {
            background-color: #f08c35;
            border-color: #f08c35;
            border-radius: 2px;
            color: #ffffff;
            padding-top: 4px;
            padding-bottom: 4px;
            padding-right: 12px;
            padding-left: 12px;
        }
        .avatar {
            padding-left: 30px;
            padding-right: 0px;
            width: 80px;
        }
        .roundCorner {
          width: 40px;
          height: 40px;
          -moz-border-radius: 20px;      
          -webkit-border-radius: 20px;  
          border-radius: 20px;         
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
# movie_tile_content = '''
# <div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
#     <img src="{poster_image_url}" width="220" height="342">
#     <h2>{movie_title}</h2>
# </div>
# '''
movie_tile_content = '''
<div class="col-md-6 col-lg-4  text-center flip-container  movie-tile " data-trailer-youtube-id="{trailer_youtube_id}" >
    <div class="front">
        <img src="{poster_image_url}" width="220" height="342">
        <h2>{movie_title}</h2>
    </div>

    <div class="back">
        <h3 class="text-center">Director</h3>
        <div class="row">
            <div class="col-md-3 avatar">
                <img class="roundCorner" src="{director_image_url}" alt="avatar">
            </div>
            <div class="col-md-9">
                <h4 class="text-left">{director_name}</h4>
            </div>
        </div>
        <hr>
        <h3 class="text-center">Main Actor</h3>
        <div class="row">
            <div class="col-md-3 avatar">
                <img class="roundCorner" src="{actor_image_url}" alt="avatar">
            </div>
            <div class="col-md-9">
                <h4 class="text-left">{actor_name}</h4>
            </div>
        </div>
        <hr>
        <p>{movie_storyline}</p>
        <div class="text-center">
            <label class="btn-primary"   data-toggle="modal" data-target="#trailer">Show Trailer</label>
        </div>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_storyline=movie.storyline,
            director_image_url=movie.director.avatar_url,
            director_name=movie.director.name,
            actor_image_url=movie.main_actor.avatar_url,
            actor_name=movie.main_actor.name
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)