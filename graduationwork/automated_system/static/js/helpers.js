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


function genericSuccess (result) { console.log(`success: ${result}`) }
function genericFailure (result) { console.log(`failure: ${result}`) }
