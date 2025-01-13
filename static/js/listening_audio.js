document.addEventListener('DOMContentLoaded', function () {
    let audioElements = document.querySelectorAll('audio');
    let popup = document.querySelector('.popup');
    let playButton = document.querySelector('#playAudio');
    let form = document.getElementById('preguntas'); // Get the form element

    playButton.addEventListener('click', function () {
        popup.style.display = 'none'; // Hide the popup

        // Introduce a delay of 5 seconds before starting the audio
        setTimeout(function () {
            // Play the first audio and set up the sequence
            if (audioElements.length > 0) {
                let currentAudioIndex = 0;

                audioElements[currentAudioIndex].play();
                audioElements[currentAudioIndex].addEventListener('ended', function playNext() {
                    currentAudioIndex++;
                    if (currentAudioIndex < audioElements.length) {
                        audioElements[currentAudioIndex].play();
                        audioElements[currentAudioIndex].addEventListener('ended', playNext);
                    } else {
                        // After all audios have finished, wait for 10 minutes and then submit the form
                        setTimeout(function () {
                            // Submit the form after 10 minutes
                            form.submit();
                        }, 10 * 60 * 1000); // 10 minutes = 10 * 60 * 1000 milliseconds
                    }
                });
            }
        }, 5000); // 5000 milliseconds = 5 seconds
    });

    window.addEventListener('beforeunload', function (event) {
        event.preventDefault(); // Prevent the default behavior
        event.returnValue = ''; // Standard approach for modern browsers
    });
});
