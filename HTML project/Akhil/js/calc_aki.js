				
function multiply()
{	
	let a=document.getElementById("data1").value;
	let b=document.getElementById("data2").value;
	var c;
	c=a*b;
	document.getElementById("data3").value=c;
}

function divide()
{	
	let a=document.getElementById("data1").value;
	let b=document.getElementById("data2").value;
	var c;
	c=a/b;
	document.getElementById("data3").value=c;
}


function substract()
{	
	let a=document.getElementById("data1").value;
	let b=document.getElementById("data2").value;
	var c;
	c=a-b;
	document.getElementById("data3").value=c;
}

function add()
{	
	let a=Number(document.getElementById("data1").value);
	let b=Number(document.getElementById("data2").value);
	var c;
	c=a+b;
	document.getElementById("data3").value=c;
}
						
