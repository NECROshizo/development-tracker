import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default {
  plugins: [react()],
  server: {
    port: 5173,
    open: true,
  },
};
