document.addEventListener('DOMContentLoaded', () => {
    const citiesWrapperElement = document.querySelector('[data-js-cities-wrapper]');
    const citiesCheckboxElements = citiesWrapperElement.querySelectorAll('[data-js-checkbox]');
    const emailWrapperElement = document.querySelector('[data-js-email-wrapper]')
    const emailElement = emailWrapperElement.querySelector('[data-js-email]')
    const submitButtonElement = document.querySelector('[data-js-submit]')

    const agreementCheckboxWrapperElement = document.querySelector('[data-js-agreement-checkbox-wrapper]')
    const agreementCheckboxElement = agreementCheckboxWrapperElement.querySelector('[data-js-agreement-checkbox]')
    
    citiesWrapperElement.addEventListener('click', () => {
        for(let element of citiesCheckboxElements) {
            // console.log(element)
            if(element.checked) {
                citiesWrapperElement.classList.remove('field__wrapper--error')
                return;
            }
        }
    })

    emailElement.addEventListener('input', () => {
        emailElement.classList.remove('field__control--error')
    })

    agreementCheckboxWrapperElement.addEventListener('click', () => {
        if(agreementCheckboxElement.checked) {
            agreementCheckboxWrapperElement.classList.remove('field__wrapper--error')
        }
    })

    function checkCitites(event) {
        for(let element of citiesCheckboxElements) {
            // console.log(element)
            if(element.checked) {
                return;
            }
        }
        event.preventDefault();
        citiesWrapperElement.classList.add('field__wrapper--error')
    }

    function checkEmail(event) {
        if(emailElement.value.length === 0) {
            emailElement.classList.add('field__control--error')
            emailWrapperElement.dataset.errorMsg = 'Обязательное поле'
            event.preventDefault();
        }
        else if (!emailElement.checkValidity()) {
            emailElement.classList.add('field__control--error')
            emailWrapperElement.setAttribute('data-error-msg', 'Введите правильный адрес почты');
            event.preventDefault();
        }
    }
    function checkAgreement(event) {
        if(!agreementCheckboxElement.checked) {
            agreementCheckboxWrapperElement.classList.add('field__wrapper--error')
            event.preventDefault()
        }
    }

    submitButtonElement.addEventListener('click', (e) => {
        checkCitites(e)
        checkEmail(e)
        checkAgreement(e)
    })
})