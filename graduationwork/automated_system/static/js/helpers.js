function ajaxRequest (url, action, payload, resultHandler) {
  let csrftoken = Cookies.get('csrftoken')
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (!(/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type)) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken)
      }
    }
  })
  payload = JSON.stringify(payload)
  $.ajax({
    url,
    type: "POST",
    data: { action, payload },
    success: resultHandler
  })
}


function ajaxRequestFile (url, data, resultHandler) {
  let csrftoken = Cookies.get('csrftoken')
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (!(/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type)) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken)
      }
    }
  })
  $.ajax({
    url,
    type: "POST",
    cache: false,
    contentType: false,
    processData: false,
    data,
    success: resultHandler
  })
}


function genericResultHandler (result, successHandler = genericSuccess, failureHandler = genericFailure) {
  result = JSON.parse(result)
  result.success
    ? successHandler(result.success)
    : failureHandler(result.failure)
}


let successTimeout = undefined

function genericSuccess (result) {
  const successInnerHTML = `
    Успех
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>`

  const prevFailureBox = document.getElementById('failure-alert-box')
  if (prevFailureBox) { prevFailureBox.remove() }

  clearTimeout(successTimeout)

  const prevSuccessBox = document.getElementById('success-alert-box')
  if (prevSuccessBox) {
    prevSuccessBox.innerHTML = successInnerHTML
  } else {
    const mainBodyDOM = document.getElementById('main-body')
    const successBox = document.createElement('div')
    successBox.classList.add('alert', 'alert-success', 'fixed-top')
    successBox.role = "alert"
    successBox.id = 'success-alert-box'
    successBox.innerHTML = successInnerHTML
    mainBodyDOM.insertBefore(successBox, mainBodyDOM.firstChild)
  }
  successTimeout = setTimeout(() => {
    $(".alert").alert('close')
    successTimeout = undefined
  }, 3000)
}

function genericFailure (result) {
  const failureInnerHTML = `
    ${result}
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>`

  const prevSuccessBox = document.getElementById('success-alert-box')
  if (prevSuccessBox) { prevSuccessBox.remove() }

  clearTimeout(successTimeout)

  const prevFailureBox = document.getElementById('failure-alert-box')
  if (prevFailureBox) {
    prevFailureBox.innerHTML = failureInnerHTML
  } else {
    const mainBodyDOM = document.getElementById('main-body')
    const failureBox = document.createElement('div')
    failureBox.classList.add('alert', 'alert-danger', 'fixed-top')
    failureBox.role = "alert"
    failureBox.id = 'failure-alert-box'
    failureBox.innerHTML = failureInnerHTML
    mainBodyDOM.insertBefore(failureBox, mainBodyDOM.firstChild)
  }
}
