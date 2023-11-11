async function SearchDatabase() {
    
    // data sent from the POST request
    var formData = new FormData(document.forms[0])

    // get all form keys and values
    var obj = Object.fromEntries(Array.from(formData.keys())
        .map(key => [key, formData.getAll(key).length > 1 ?
            formData.getAll(key) : formData.get(key)]))
            
    var jsonreq = (`${JSON.stringify(obj)}`)
    
    try {
        var response = await fetch('http://127.0.0.1:8000/return_pieces/', {
        method: "POST",
        body: jsonreq,
        headers: {"Content-type": "application/json; charset=UTF-8"}
  });
      }
      catch(err) {
        alert("Oops... Check that the backend server (uvicorn) is started and try again!")
        console.log("The error is: " + err);
        //document.getElementById("demo").innerHTML = err.message;
      }
    
  const responseJson = await response.json();
  //console.log(responseJson); // logs 'OK'
  
  //var index_author = document.getElementById("author_name");
  //var index_creation = document.getElementById("creation_date"); 
  //index_author.style.color = "blue";
  //index_creation.style.color = "green"; 

  var index_reslen = document.getElementById("res_len"); 
  
  let res_length = responseJson.res.length

  index_reslen.innerHTML = (res_length);

  let parent = document.getElementById("parent_results");
  
  document.querySelectorAll(".piece_detail").forEach(el => el.remove());
  
  for (let i = 0; i <= res_length - 1; i++) {
    let piece = responseJson.res[i];
    // Piece div creation
	let div = document.createElement('div');
    div.setAttribute('class', "piece_detail");
    // Piece title creation
    let title = document.createElement('h4');
    
    title.textContent = piece.name;
    div.appendChild(title);

    let information = document.createElement('p');
    information.textContent = piece.author + " - " + piece.creation_date;

    let link = document.createElement('a');
    link.href = piece.url;
    link.target="_blank";

    let image = document.createElement('img');
    image.src = "images/" + (i + 1) + ".jpg";
    //image.src = "images/" + (i + 1) + ".jpg";

    let description = document.createElement('p');
    description.setAttribute('class', "piece_description");
    description.textContent = "Here will come a description of the piece and detail, Here will come a description of the piece and detail, Here will come a description of the piece and detail"

    let div_image_description = document.createElement('div');
    div_image_description.setAttribute('class', "image_description");



    link.appendChild(image);
    div_image_description.appendChild(link);
    div_image_description.appendChild(description);
    div.appendChild(div_image_description);
    div.appendChild(information);

	parent.appendChild(div);
}
}

