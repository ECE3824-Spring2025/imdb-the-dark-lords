import { useEffect } from 'react';

function MovieList() {
  useEffect(() => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) {
          entry.target.classList.add('fade-out');
        } else {
          entry.target.classList.remove('fade-out');
        }
      });
    }, {
      threshold: 0.1,
    });

    // Observe each movie item
    document.querySelectorAll('.movie-item').forEach(item => {
      observer.observe(item);
    });

    // Cleanup on component unmount
    return () => {
      document.querySelectorAll('.movie-item').forEach(item => {
        observer.unobserve(item);
      });
    };
  }, []);

  return (
    <div className="movie-list">
      <div className="movie-item">
        <img src="movie-poster.jpg" alt="Movie Poster" />
        <h3>Movie Title</h3>
      </div>
      {/* Add more movie items */}
    </div>
  );
}

export default MovieList;

function toggleDropdown() {
    document.getElementById("genreDropdown").classList.toggle("show");
}

function selectGenre(genre) {
    // Update button text
    document.getElementById("dropdownButton").textContent = genre.charAt(0).toUpperCase() + genre.slice(1);

    // Store the selected value in hidden input (so it gets submitted)
    document.getElementById("selectedGenre").value = genre;

    // Close dropdown after selection
    document.getElementById("genreDropdown").classList.remove("show");
}

// Close dropdown if clicked outside
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn') && !event.target.closest('.dropdown-content')) {
        document.getElementById("genreDropdown").classList.remove("show");
    }
};

// Preserve selection after form submission
document.addEventListener("DOMContentLoaded", function () {
    const params = new URLSearchParams(window.location.search);
    const selectedGenre = params.get("genre");

    if (selectedGenre) {
        document.getElementById("dropdownButton").textContent = selectedGenre.charAt(0).toUpperCase() + selectedGenre.slice(1);
        document.getElementById("selectedGenre").value = selectedGenre;
    }
});



