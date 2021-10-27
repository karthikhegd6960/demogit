function insertvalue(){
	var select1=document.getElementById("purpose"),
	    txtval=document.getElementById("val").value,
	    newoption=document.createElement("OPTION"),
	    newoptionval=document.createTextNode(txtval);

	newoption.appendChild(newoptionval);
	purpose.insertBefore(newoption,select1.lastChild);
	

}

function addoption(selectId, value, text) {
    var html = '<option value="'+value+'">'+text+'</option>';
    
    $('#'+'selectId').append(html);
}