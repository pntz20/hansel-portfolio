// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// Contact form handling (works with Formspree)
const form = document.getElementById('contact-form');
const formStatus = document.getElementById('form-status');

if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Show loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalBtnText = submitBtn.innerHTML;
    submitBtn.innerHTML = '⏳ Sending...';
    submitBtn.disabled = true;
    
    const formData = new FormData(form);
    
    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
          'Accept': 'application/json'
        }
      });
      
      if (response.ok) {
        formStatus.innerHTML = '<div class="form-success">✅ Message sent! I\'ll reply within 24 hours.</div>';
        form.reset();
      } else {
        const data = await response.json();
        if (data.errors) {
          formStatus.innerHTML = '<div class="form-error">❌ Oops! Something went wrong. Please try again.</div>';
        } else {
          formStatus.innerHTML = '<div class="form-error">❌ Something went wrong. Please email me directly at hansel@yourdomain.com</div>';
        }
      }
    } catch (error) {
      formStatus.innerHTML = '<div class="form-error">❌ Network error. Please check your connection and try again.</div>';
    }
    
    // Reset button
    submitBtn.innerHTML = originalBtnText;
    submitBtn.disabled = false;
    
    // Clear status message after 5 seconds
    setTimeout(() => {
      formStatus.innerHTML = '';
    }, 5000);
  });
}

// Add a small console log to confirm JS loaded
console.log('Portfolio site loaded — ready for clients!');