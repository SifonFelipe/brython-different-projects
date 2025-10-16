// Copy code button functionality
document.querySelectorAll('.code-copy').forEach(button => {
    button.addEventListener('click', function() {
        const codeBlock = this.closest('.code-block').querySelector('code');
        const text = codeBlock.textContent;
        
        navigator.clipboard.writeText(text).then(() => {
            this.textContent = 'Copied!';
            setTimeout(() => {
                this.textContent = 'Copy';
            }, 2000);
        });
    });
});
