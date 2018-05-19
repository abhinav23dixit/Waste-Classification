<!DOCTYPE html>
<html>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway">
<head>
	<title>Result</title>
	<style type="text/css">
		body {
             background-image: url("2.jpg");
                background-size: cover;
                height:auto;
        background-repeat: no-repeat;
        background-blend-mode:multiply;
        background-color: #505050;
        font-family: "Raleway", sans-serif;
			background-color: #505050;
			text-align: center;
			color: white;
			font-size: 25px;
		}
        #chart{
            display: block;
            float:right;
            padding-right: 125px;
                        
        }
        #new{
            max-width: 600;
            max-height: 400;
            
        }
	</style>
	<link href="https://fonts.googleapis.com/css?family=Rokkitt" rel="stylesheet">
	<script type = "text/javascript" src = "https://www.gstatic.com/charts/loader.js"></script>
	<script type = "text/javascript">google.charts.load('current', {packages: ['corechart']});</script>
</head>
<body>
	<h2 style="font-size:50px">RESULT</h2>

	<?php
		$filename = "C://Users//John//Desktop//new.txt";
		$lines = file($filename, FILE_IGNORE_NEW_LINES);
		$arr = ['Containers','Leaf','Metal','Paper','Plastic'];
	?>
	<div id="chart"></div>
	<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
	<script type="text/javascript">
		google.charts.load('current', {'packages':['corechart']});
		google.charts.setOnLoadCallback(drawChart);

		function drawChart() {
			var data = google.visualization.arrayToDataTable([
			['Element', 'Percentage	', { role: 'style' }, { role: 'annotation' } ],
			['Containers', <?php echo "$lines[0]"; ?>, 'blue', '<?php echo "$lines[0]"; ?>' ],
			['Leaf', <?php echo "$lines[1]"; ?>, 'silver', '<?php echo "$lines[1]"; ?>' ],
			['Metal', <?php echo "$lines[2]"; ?>, 'red', '<?php echo "$lines[2]"; ?>' ],
			['Paper', <?php echo "$lines[3]"; ?>, 'green', '<?php echo "$lines[3]"; ?>' ],
			['Plastic', <?php echo "$lines[4]"; ?>, 'color: orange', '<?php echo "$lines[4]"; ?>' ]
		]);

			var options = {'title':'Garbage Classification', 'width':600, 'height':400};

			var chart = new google.visualization.BarChart(document.getElementById('chart'));
			chart.draw(data, options);
		}
	</script>
    <div id="new">
    <img src="uploads/file.jpg" width="600px" height="400px">
    </div>
    <br>
    <br>
 
  
    
    <?php
		$max = max($lines);
		$index = array_search($max, $lines);
		echo "<h2>Highest probability: $arr[$index]</h2>";
	?>
</body>
</html>