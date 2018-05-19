<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<head>
    <script>
           function newfun() {
            var x = document.getElementById("prog");
            if (x.style.display === "none") {
                x.style.display = "block";
            } else {
                x.style.display = "none";
            }
           } 
    </script>
    
<link href="https://fonts.googleapis.com/css?family=Rokkitt" rel="stylesheet">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>


<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/css/materialize.min.css">

    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-beta/js/materialize.min.js"></script>
            
    
  <title>Image Classification</title>
  <style type="text/css">
     
  body {
      background-image: url("2.jpg");
        
        
          background-position: center;
          background-repeat: no-repeat;
          background-size: 100%;
        position: relative;
           background-blend-mode:multiply;
    
          
   background-color: #505050;
    font-family: "Raleway", sans-serif;
  }
      #prog{
          margin-top: auto;
          width: 300px;
          margin-left: 615px;
          display:none;
      }
      
     
  .header {
    color: white;
      text-align: center;
    font-size: 40px;
  }
      .header2{
          color:white;
          text-align: center;
          font-size: 30px;
      }
      
    form {
        text-align: center;
        font-size: 40px;
    }
  </style>
</head>
<body>
     <h1 class="header" style="margin-top: 150px;"><u>Waste Image Classifier</u></h1>
  <p class="header2" style="margin-top:100px;">Upload the image of Waste you want to Classify</p>

  <form action="upload.php" method="post" enctype="multipart/form-data" style="padding-top: auto;"><br>
      <input type="file" name="file" style="font-size: 30px;color: white;margin-left:auto; margin-right:auto;" accept=".jpg, .png, .jpeg"; />
    <br><br>
    <button id="submit" type="submit" class="btn" onclick="newfun()" name="submit" style="background-color: white;color: black;font-size: 30px;margin:auto">Upload</button><br>
      <br>
     <div id="prog" class="progress" style="display:none;" >
      <div class="indeterminate" style="margin-top:auto;"></div>
  </div>

  </form>
  


</body>
</html>