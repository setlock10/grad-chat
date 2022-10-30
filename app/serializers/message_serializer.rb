class MessageSerializer < ActiveModel::Serializer
  attributes :id, :time, :text 
  has_one :user
end
