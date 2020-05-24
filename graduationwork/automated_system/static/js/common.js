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
