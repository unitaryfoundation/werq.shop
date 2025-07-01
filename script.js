document.addEventListener("DOMContentLoaded", () => {
  const triggers = document.querySelectorAll(".popover-trigger");

  triggers.forEach(trigger => {
    const popover = document.createElement("div");
    popover.className = "popover";
    popover.textContent = trigger.getAttribute("data-popover");
    document.body.appendChild(popover);

    trigger.addEventListener("click", e => {
      e.stopPropagation();
      const rect = trigger.getBoundingClientRect();
      popover.style.top = `${rect.bottom + window.scrollY + 5}px`;
      popover.style.left = `${rect.left + window.scrollX}px`;
      popover.style.display = "block";

      const closePopover = () => {
        popover.style.display = "none";
        document.removeEventListener("click", closePopover);
      };
      setTimeout(() => document.addEventListener("click", closePopover), 0);
    });
  });
});
