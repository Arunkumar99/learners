<html>
<head>
<script type="javascript">
function disableBackButton()
{
setTimeout("preventPageLoad()",1);
}
function preventPageLoad()
{
try{
history.forward();
}catch(e){
}
setTimeout("prevenPageLoad()",200);
}
</script>
</head>
<body onLoad="backButtonOverride()">
<h1>Hello </h1>
</body>
</html>

