class CreateMessages < ActiveRecord::Migration[7.0]
  def change
    create_table :messages do |t|
      t.integer :user_id
      t.string :time
      t.text :text

      t.timestamps
    end
  end
end
