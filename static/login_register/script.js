const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

// Disable transitions initially
document.addEventListener('DOMContentLoaded', () => {
    const formState = localStorage.getItem('formState');

    // Disable transitions temporarily
    container.style.transition = 'none';

    // Set the initial state without sliding
    if (formState === 'signUp') {
        container.classList.add('right-panel-active');
    } else {
        container.classList.remove('right-panel-active');
    }

    // Enable transitions after setting the initial state
    setTimeout(() => {
        container.style.transition = ''; // Re-enable the transition
    }, 0);
});

// Add click event for Sign Up button
signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
    localStorage.setItem('formState', 'signUp');
});

// Add click event for Sign In button
signInButton.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
    localStorage.setItem('formState', 'signIn');
});
