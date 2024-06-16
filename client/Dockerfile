# Use an official Node.js runtime as a parent image
FROM node:16

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 5173 (default Vite port)
EXPOSE 5173

# Run Vite development server
CMD ["npm", "run", "dev", "--", "--host"]


# # frontend/Dockerfile

# # Use an official Node.js runtime as a parent image
# FROM node:16

# # Set the working directory in the container for the frontend
# WORKDIR /app

# # Copy package.json and package-lock.json to the working directory
# COPY package*.json ./

# # Install frontend dependencies
# RUN npm install

# # Copy the rest of the frontend code to the working directory
# COPY . .

# # Build the frontend
# RUN npm run build

# # Use nginx as the web server for serving the frontend
# FROM nginx:1.21

# # Copy the built frontend code to the nginx server
# COPY --from=0 /app/dist /usr/share/nginx/html

# # Expose port 80 for the nginx server
# EXPOSE 80

# # Start nginx
# CMD ["nginx", "-g", "daemon off;"]
