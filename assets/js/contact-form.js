const form = document.querySelector("[data-contact-form]");
const statusBox = document.querySelector("[data-form-status]");
const submitButton = form?.querySelector('button[type="submit"]');

if (form && statusBox && submitButton) {
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    statusBox.textContent = "Sending your request…";
    statusBox.className = "form-status is-sending";
    submitButton.disabled = true;

    const formData = new FormData(form);
    const payload = Object.fromEntries(formData.entries());

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const result = await response.json();

      if (!response.ok || !result.ok) {
        throw new Error(result.message || "Unable to send your request.");
      }

      statusBox.textContent = result.message;
      statusBox.className = "form-status is-success";
      form.reset();
    } catch (error) {
      statusBox.textContent =
        error.message || "Unable to send your request. Please try again.";
      statusBox.className = "form-status is-error";
    } finally {
      submitButton.disabled = false;
    }
  });
}
