async function SearchDatabase() {
    
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
  
  //var index_author = document.getElementById("author_name");
  //var index_creation = document.getElementById("creation_date"); 
  //index_author.style.color = "blue";
  //index_creation.style.color = "green"; 

  var index_reslen = document.getElementById("res_len"); 
  
  let res_length = responseJson.res.length

  index_reslen.innerHTML = (res_length);

  let parent = document.getElementById("parent_results");

  for (let i = 0; i <= res_length; i++) {
    // Piece div creation
	let div = document.createElement('div');
    div.setAttribute('class', "piece_detail");
    // Piece title creation
    let title = document.createElement('h4');
    title.textContent = responseJson.res[i].name;
    div.appendChild(title);

    let information = document.createElement('p');
    information.textContent = responseJson.res[i].author + " - " + responseJson.res[i].creation_date ;

    let link = document.createElement('a');
    link.href = responseJson.res[i].url;
    link.target="_blank";

    let image = document.createElement('img');
    image.src = "images/cheztortoni.jpg";

    link.appendChild(image)
    
    div.appendChild(information);

    div.appendChild(link);

	parent.appendChild(div);
}
}

