class ApplicationController < ActionController::API
    include ActionController::Cookies
    rescue_from ActiveRecord::RecordNotFound, with: :render_not_found_response
    rescue_from ActiveRecord::RecordInvalid, with: :render_unprocessable_entity_response

 
    def hello_world
        session[:count] = (session[:count] || 0) + 1
        render json: { count: session[:count] }
      end
    

      
      private

      def authorize
          @current_user ||=User.find_by(id: session[:user_id])
          render json: {errors: ["Not Authorized"]}, status: :unauthorized unless @current_user
      end
  
      def authenticated_user
  
          render json: {errors: ["Not Logged In"]}, status: :unauthorized unless @current_user
      end
        
      def render_not_found_response(invalid)
          render json: {errors: invalid}, status: :not_found
      end

      def render_unprocessable_entity_response(invalid)
          render json: {errors: invalid.record.errors}, status: :unprocessable_entity
      end
  
  
end
