/** @type {import('tailwindcss').Config} */
module.exports = {
  variants: {
    extend: {
      opacity: ['disabled'],
      cursor: ['disabled'],
      animation:{
        spin: 'spin 1s linear infinite',
      }
    }
  },
  content: ["./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {},
  },
  plugins: [],
}

