async function SubmitVars() {
    
    // data sent from the POST request
    var formData = new FormData(document.forms[0])

    // get all form keys and values
    var obj = Object.fromEntries(Array.from(formData.keys())
        .map(key => [key, formData.getAll(key).length > 1 ?
            formData.getAll(key) : formData.get(key)]))
            
    var jsonreq = (`${JSON.stringify(obj)}`)

    const response = await fetch('http://127.0.0.1:8000/return_sum/', {
    method: "POST",
    body: jsonreq,
    headers: {"Content-type": "application/json; charset=UTF-8"}
  })

  const responseJson = await response.json();
  console.log(responseJson); // logs 'OK'
  
  var index_author = document.getElementById("author_name");
  var index_creation = document.getElementById("creation_date"); 
  var index_reslen = document.getElementById("res_len"); 
  
  index_author.style.color = "blue";
  index_creation.style.color = "green";  
  
  index_reslen.innerHTML = (responseJson.res_length);
  index_author.innerHTML = (responseJson.Author);
  index_creation.innerHTML = (responseJson.Creation_date);
}