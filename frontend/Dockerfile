# Use official Node image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files and install
COPY package*.json ./
RUN npm install

# Copy frontend code
COPY . .

# Expose React port
EXPOSE 3000

# Start React app
CMD ["npm", "start"]
