import React, { useState, useEffect } from 'react';

function MovieList() {
  const [selectedGenre, setSelectedGenre] = useState('');
  const [modalMovie, setModalMovie] = useState(null);
  const [dropdownOpen, setDropdownOpen] = useState(false);

  // Intersection Observer for fade-out effect
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

  // Handle modal open
  const openModal = (movie) => {
    setModalMovie(movie);
  };

  // Handle modal close
  const closeModal = () => {
    setModalMovie(null);
  };

  // Handle click outside modal
  const handleOutsideClick = (e) => {
    if (e.target.classList.contains('modal')) {
      closeModal();
    }
  };

  // Function to toggle dropdown visibility
  const toggleDropdown = () => {
    const dropdown = document.getElementById("genreDropdown");
    dropdown.classList.toggle("show");
  };

  // Function to handle genre selection
  const selectGenre = (genre) => {
    setSelectedGenre(genre);
    setDropdownOpen(false); // Close dropdown after selecting
  };

  return (
    <div>
      {/* Genre Dropdown */}
      <div className="dropdown">
        <button onClick={toggleDropdown} className="dropbtn" id="dropdownButton">Select Genre</button>
        <div className={`dropdown-content ${dropdownOpen ? 'show' : ''}`} id="genreDropdown">
          <a href="#" onClick={() => selectGenre('action')}>Action</a>
          <a href="#" onClick={() => selectGenre('comedy')}>Comedy</a>
          <a href="#" onClick={() => selectGenre('drama')}>Drama</a>
        </div>
      </div>

      {/* Movie List */}
      <div className="movie-list">
        <div className="movie-item">
          <img src="movie-poster.jpg" alt="Movie Poster" onClick={() => openModal({ title: 'Movie Title', rating: '5.5', poster: 'movie-poster.jpg' })} />
          <h3 className="movie-name">Movie Title</h3>
          <p className="movie-rating">5.5</p>
        </div>
        {/* Add more movie items here */}
      </div>

      {/* Movie Modal */}
      {modalMovie !== null && modalMovie.title && (
        <div className="modal" onClick={handleOutsideClick}>
          <div className="modal-content">
            <span className="close" onClick={closeModal}>&times;</span>
            <h2>{modalMovie.title}</h2>
            <img src={modalMovie.poster} alt="Movie Poster" />
            <p>Rating: {modalMovie.rating}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default MovieList;
