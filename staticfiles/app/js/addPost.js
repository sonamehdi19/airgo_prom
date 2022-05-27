const postContainer = document.querySelector(".posts-container");
const btnSender = document.querySelector(".sender-submit");
const btnCarrier = document.querySelector(".carrier-submit");

btnCarrier?.addEventListener("click", function (e) {
  e.preventDefault();
  
  const from = document.querySelector("#carrier-from");
  const departure = document.querySelector("#carrier-departure");
  const to = document.querySelector("#carrier-to");
  const arrival = document.querySelector("#carrier-arrival");
  const phone = document.querySelector("#carrier-phone");
  const note = document.querySelector("#carrier-note");
  const csrf_token =  document.querySelector('[name="csrfmiddlewaretoken"]').value;
  console.log('CSRF '+csrf_token);

  // Creating variable form_data to save the carry post data and submit it to backend
  var form_data = new FormData();
  form_data.append('from', from.value);
  form_data.append('departure', departure.value);
  form_data.append('to', to.value);
  form_data.append('arrival', arrival.value);
  form_data.append('phone', phone.value);
  form_data.append('note', note.value);
  form_data.append('csrfmiddlewaretoken', csrf_token);

  // Fetch call to send data to backend
  fetch(``, {
    method: 'POST',
    body: form_data
  })
  .then(response => response.json())
  .then(data => {
    if(data.success){
      console.log('Success:', data);
      const alertBox = document.querySelector('.alert');
      alertBox.style.display = 'block';
      alertBox.classList.remove('alert-danger');
      alertBox.classList.add('alert-success');
      document.querySelector('.error-msg').innerHTML = data.message;
      const html = `
        <div class="post">
        <header class="post--carrier"><p>Carrier</p></header>
        <div class="post__detail">
            <span>Location:</span>
            <p>${from.value}</p>
        </div>
        <div class="post__detail">
            <span>Departure date:</span>
            <p>${departure.value}</p>
        </div>
        <div class="post__detail">
            <span>Destination:</span>
            <p>${to.value}</p>
        </div>
        <div class="post__detail">
            <span>Arrival date:</span>
            <p>${arrival.value}</p>
        </div>
        <div class="post__detail">
            <span>Contact number:</span>
            <p>${phone.value}</p>
        </div>
        <div class="post__detail">
            <span>Additional note:</span>
            <p>${note.value}</p>
        </div>
        </div>
      `;

      if (validation.isValid(".add__carrier")) {
        // document.querySelector(".no-post").style.display = "none";
        postContainer.insertAdjacentHTML("afterbegin", html);
        document
          .querySelectorAll(".add__carrier input")
          .forEach((el) => (el.value = ""));
        document.querySelector(".add__carrier textarea").value = "";
      }
    }
    else {
      const alertBox = document.querySelector('.alert');
      alertBox.style.display = 'block';
      alertBox.classList.remove('alert-success')
      alertBox.classList.add('alert-danger');
      document.querySelector('.error-msg').innerHTML = data.message;
    }
    
  })
  .catch(error => {
    console.error('Error:', error);
  });
});

btnSender?.addEventListener("click", function (e) {
  e.preventDefault();
  const from = document.querySelector("#id_location");
  const to = document.querySelector("#id_destination");
  const due = document.querySelector("#id_due_date");
  const phone = document.querySelector("#id_contact_number");
  const item = document.querySelector("#id_add_image");
  const note = document.querySelector("#id_additional_note");

  const file = item.files[0];
  const url = URL.createObjectURL(file);
  console.log('Item: '+item.files[0])
  console.log('File:  '+file)
  const csrf_token =  document.querySelector('[name="csrfmiddlewaretoken"]').value;
  console.log('CSRF '+csrf_token);

  // Creating variable form_data to save the carry post data and submit it to backend
  var form_data = new FormData();
  form_data.append('from', from.value);
  form_data.append('to', to.value);
  form_data.append('due', due.value);
  form_data.append('phone', phone.value);
  form_data.append('note', note.value);
  form_data.append('item', file);
  form_data.append('csrfmiddlewaretoken', csrf_token);

  // Fetch call to send data to backend
  fetch(``, {
    method: 'POST',
    body: form_data
  })
  .then(response => response.json())
  .then(data => {
    if(data.success){
      console.log('Success:', data);
      const alertBox = document.querySelector('.alert');
      alertBox.style.display = 'block';
      alertBox.classList.remove('alert-danger');
      alertBox.classList.add('alert-success');
      document.querySelector('.error-msg').innerHTML = data.message;
      const html = `
          <div class="post">
          <header class="post--sender"><p>Sender</p></header>
          <div class="post__detail">
            <span>Location:</span>
            <p>${from.value}</p>
          </div>
          <div class="post__detail">
            <span>Destination:</span>
            <p>${to.value}</p>
          </div>
          <div class="post__detail">
            <span>Due date:</span>
            <p>${due.value}</p>
          </div>
          <div class="post__detail">
            <span>Contact number:</span>
            <p>${phone.value}</p>
          </div>
          <div class="post__detail">
            <span>Sending item:</span>
            <a href="${url}" target="_blank" rel="noopener">Image</a>
          </div>
          <div class="post__detail">
            <span>Additional note:</span>
            <p>${note.value}</p>
          </div>
        </div>
        `;

      if (validation.isValid(".add__sender")) {
        // document.querySelector(".no-post").style.display = "none";
        postContainer.insertAdjacentHTML("afterbegin", html);
        document
          .querySelectorAll(".add__sender input")
          .forEach((el) => (el.value = ""));
        document.querySelector(".add__sender textarea").value = "";
      }
    }
    else {
      const alertBox = document.querySelector('.alert');
      alertBox.style.display = 'block';
      alertBox.classList.remove('alert-success')
      alertBox.classList.add('alert-danger');
      document.querySelector('.error-msg').innerHTML = data.message;
    }
    
  })
  .catch(error => {
    console.error('Error:', error);
  });
});


