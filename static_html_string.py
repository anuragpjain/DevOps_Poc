""""This return the HTML to browser for accepting input """
HTML = """
    <html>
<body style="background-color:powderblue;">
<center>
<h2>INPUT VALUE:Hours and Minutes</h2>

<form  onsubmit="myFunction()">
  <label for="hrs">Hours:</label><br>

  <input type="number"  max="12"  id="hrs"  name="hours"  value="" ><br>

  <label for="mnt">Minutes:</label><br>

  <input type="number"  max="60"  id="mnt"  name="minute" value="" ><br><br>

    <button type="button" onclick="myFunction()">Get Angle</button>
</form>

 <p id="test" > <b>Angle between hours and minutes is <label id="angle"></label> </b></p>
<p id="demo"></p></center>
<script>


function myFunction() {
var request = new XMLHttpRequest();

try{
    var hourValue = document.getElementById('hrs').value;
    var minuteValue = document.getElementById('mnt').value;
	var url = "https://clock-angle-icbqkvt2oa-ue.a.run.app/angle.cal?hour="+hourValue+"&min="+minuteValue;
	request.open('GET',url, false);
	//request.open('GET','https://clock-angle-icbqkvt2oa-ue.a.run.app/angle.cal?hour=4&min=00', false);
	request.send();
	}catch(err) {
  document.getElementById("demo").innerHTML = err.message;
}
var responseText = JSON.parse(request.responseText);
    document.getElementById("angle").innerHTML = responseText.response;
   
    }
</script>

</body>
</html>
"""
