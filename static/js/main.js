window.addEventListener('DOMContentLoaded', function() {
	// кнопка в избранное на карточке товара
	let hearts = document.querySelectorAll('.product-card__fav-btn');
	for (let i=0; i<hearts.length; i++) {
		let heart = hearts[i]
		heart.addEventListener('click', function() {
			heart.classList.toggle('active')
		})
	}
});

// рэндж слайдер цены
const rangeSlider = document.getElementById('range-slider')
	if (rangeSlider) {

		noUiSlider.create(rangeSlider, {
		    start: [0, 99999],
		    connect: true,
		    step: 1,
		    range: {
		        'min': 0,
		        'max': 99999
		    }
		});
		const priceFrom = document.getElementById('price-from');
		const priceTo = document.getElementById('price-to');
		const inputs = [priceFrom, priceTo];
		rangeSlider.noUiSlider.on('update', function(values, handle) {
				inputs[handle].value = Math.round(values[handle]);
		});
	}

let body =  document.querySelector('.body');
let modalBackdrop =  document.querySelector('.modal-dialog__backdrop');
let modalCloseBtns = 	modalBackdrop.querySelectorAll('.btn__close-modal');
let continueBtn = 	modalBackdrop.querySelector('.btn__continue');
let cartBtns = 	document.querySelectorAll('.product-card__cart');
let cartModal  = modalBackdrop.querySelector('.add-to-cart-modal')
let feedbackModal  = modalBackdrop.querySelector('.feedback-modal')
let modals = modalBackdrop.querySelectorAll('.modal')
let sendBtn = document.querySelector('.btn__send')

for (cartBtn of cartBtns) {
	cartBtn.addEventListener('click', function() {
		toggleBackDrop();
		cartModal.classList.toggle('modal-show');
	});
};

if(sendBtn) {
	sendBtn.addEventListener('click', function() {
	toggleBackDrop();
	feedbackModal.classList.toggle('modal-show');
});
}

for (modalCloseBtn of modalCloseBtns) {
	modalCloseBtn.addEventListener('click', function() {
		toggleBackDrop();
		hideModal();
	});
};

function toggleBackDrop(){
	modalBackdrop.classList.toggle('active');
};

function hideModal(){
	modals.forEach(modal => {
		modal.classList.remove('active');
	})
};

document.addEventListener('keydown', function(event) {
	if(event.keyCode == 27) {
		modalBackdrop.classList.remove('active');
		body.classList.remove('ofhidden');
		feedbackModal.classList.remove('modal-show')
		cartModal.classList.remove('modal-show')
	};
});